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
          <v-form @submit.prevent="handleEmailLogin" ref="form">
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
import { getAuth, signInWithEmailAndPassword } from 'firebase/auth'
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
          v => (v && v.length >= 6) || 'Le mot de passe doit avoir plus que 6 caractères!'
        ],
        errors: null
      }
    },
    methods: {
      handleEmailLogin () {
        signInWithEmailAndPassword(getAuth(), this.email, this.password).then((result) => {
            this.$store.dispatch('setUser', result.user)
            this.$router.push({ name: 'accueil' })
        })
      }
    },
}
</script>

<style>

</style>