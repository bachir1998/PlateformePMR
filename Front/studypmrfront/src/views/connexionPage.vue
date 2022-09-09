<template>
  <v-col cols="10" lg="4" class="mx-auto">
  <v-card class="pa-4">
    <v-card-title center>
      <div class="text-center">
      <v-avatar size="70" color="warning accent-3">
        <v-icon
        size="large"
        center
        icon="mdi-account"
      ></v-icon>
      </v-avatar>
      <h3>CONNEXION</h3>
    </div>
    </v-card-title>
          <v-form @submit.prevent="signInWithEmailAndPassword" ref="form">
            <v-card-text>
              <v-text-field
                v-model="email"
                :rules="emailRules"
                type="email"
                label="Email"
                placeholder="Email"
                prepend-inner-icon="mdi-account"
                required
              />
              <v-text-field
                v-model="password"
                :rules="passwordRules"
                :type="passwordShow?'text':'password'"
                label="Mot de passe"
                placeholder="Mot de passe"
                prepend-inner-icon="mdi-key"
                :append-icon="passwordShow ? 'mdi-eye':'mdi-eye-off'"
                @click:append="passwordShow = !passwordShow"
                required
              />
            </v-card-text>
            <v-card-actions class="justify-center">
              <v-btn type="submit" color="warning accent-3" variant="outlined">
                <span class="white--text px-8">Se connecter</span>
              </v-btn>
            </v-card-actions>
          </v-form>
          <br>
          <v-divider inset></v-divider>
          <br>
          <v-card-actions class="justify-center">
            <router-link :to="{name: 'inscriptionPage'}" style="text-decoration: none; color: black;">Vous n'avez pas encore un compte?</router-link>
          </v-card-actions>
  </v-card>
</v-col>
</template>

<script>
import axios from 'axios'
export default {
    name: 'connexionPage',
    data () {
      return {
        passwordShow: false,
        email: '',
        emailRules: [
          v => !!v || 'Veuillez entrer votre e-mail',
          v => /.+@.+\..+/.test(v) || 'Votre E-mail n\'est pas valide'
        ],
        password: '',
        passwordRules: [
          v => !!v || 'Veuillez entrer votre mot de passe',
          v => (v && v.length >= 8) || 'Le mot de passe doit avoir plus que 8 caractères!'
        ],
        errors: null
      }
    },
    methods: {
      signInWithEmailAndPassword() {
        let formData = new FormData();
        formData.append('email', this.email);
        formData.append('password', this.password);
        axios
        .post('http://localhost:8000/api/login/', formData)
        .then(result => {
          console.log(result.data.user_data[0].user_id)
          axios.get('http://localhost:8000/api/docs_checker/'+result.data.user_data[0].user_id, {headers: {"Access-Control-Allow-Origin": "*"}})
          .then((result2 => {
            let user = null
            if (result2.data.docs_checker == false) {
              if (result.data.user_data[0].type_user == 'bailleur') {
                user = {
                  'email': this.email,
                  'user_id': result.data.user_data[0].user_id,
                  'number': result.data.user_data[0].number,
                  'full_adress': result.data.user_data[0].full_adress,
                  'siret': result.data.user_data[0].siret,
                  'type_user': 'bailleur',
                  'docs_checker': false
                }
                this.$store.dispatch('setUser', user)
                this.$router.push({ name: 'profilePage', params: { idBailleur: user.user_id }})
              }
              else {
                user = {
                  'email': this.email,
                  'user_id': result.data.user_data[0].user_id,
                  'number': result.data.user_data[0].number,
                  'full_adress': result.data.user_data[0].full_adress,
                  'university': result.data.user_data[0].university,
                  'type_user': 'pmr',
                  'docs_checker': false
                }
                this.$store.dispatch('setUser', user)
                this.$router.push({ name: 'profilePMRPage', params: { idPMR: user.user_id }})
              }
            }
            else {
              if (result.data.user_data[0].type_user == 'bailleur') {
                user = {
                  'email': this.email,
                  'user_id': result.data.user_data[0].user_id,
                  'number': result.data.user_data[0].number,
                  'full_adress': result.data.user_data[0].full_adress,
                  'siret': result.data.user_data[0].siret,
                  'type_user': 'bailleur',
                  'docs_checker': true
                }
                this.$store.dispatch('setUser', user)
                this.$router.push({ name: 'bailleurPage'})
              }
              else {
                user = {
                  'email': this.email,
                  'user_id': result.data.user_data[0].user_id,
                  'number': result.data.user_data[0].number,
                  'full_adress': result.data.user_data[0].full_adress,
                  'university': result.data.user_data[0].university,
                  'type_user': 'pmr',
                  'docs_checker': true
                }
                this.$store.dispatch('setUser', user)
                this.$router.push({ name: 'PMRPage'})
              }
            }
          }))
        })
        .catch(error => console.log(error))
      }
      /**signInWithEmailAndPassword(getAuth(), this.email, this.password).then((result) => {
            this.$store.dispatch('setUser', result.data.user)
            this.$store.dispatch('setLogementsSelectionnes', this.idBailleur)
            this.$router.push({ name: 'accueil' })
        })**/
    },
    watch: {
      user(newValue){
        this.$store.dispatch('setLogements'),
        this.$store.dispatch('setLogementsSelectionnes', newValue.user_id)
      }
    },
    computed: {
      user() {
        return this.$store.state.user
      }
    }
}
</script>

<style>

</style>