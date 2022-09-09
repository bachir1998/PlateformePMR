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
      <h3>PROFILE</h3>
    </div>
    </v-card-title>
          <v-form @submit.prevent="handleProfileUpdate" ref="form">
            <v-card-text>
              <v-text-field
                v-model="email"
                :rules="emailRules"
                type="email"
                label="Email"
                placeholder="Email"
                prepend-inner-icon="mdi-account"
                disabled
              />
              <v-text-field
                v-model="number"
                :rules="numberRules"
                type="text"
                label="Number"
                placeholder="0710111213"
                prepend-inner-icon="mdi-phone"
                required
              />
              <v-text-field
                v-model="adresse"
                :rules="adresseRules"
                type="text"
                label="Adresse"
                placeholder="5bis boulevard de Berlin, 44000, Nantes"
                prepend-inner-icon="mdi-domain"
                required
              />
              <v-text-field
                v-model="universie"
                :rules="universiteRules"
                type="text"
                label="Université"
                placeholder="Université de Nantes"
                prepend-inner-icon="mdi-school"
                required
              />
            </v-card-text>
            <v-file-input
                v-model="schoolProof"
                :rules="schoolProofRules"
                accept="application/pdf"
                label="Justificatif de scolarité"
                show-size
                required
            ></v-file-input>
            <v-file-input
                v-model="PMRProof"
                :rules="PMRProofRules"
                accept="application/pdf"
                label="Justificatif de situation PMR"
                show-size
                required
            ></v-file-input>
            <v-card-actions class="justify-center">
              <v-btn type="submit" color="warning accent-3" variant="outlined">
                <span class="white--text px-8">Sauvegarder</span>
              </v-btn>
            </v-card-actions>
          </v-form>
  </v-card>
</v-col>
</template>

<script>
import axios from 'axios'
export default {
    props: ['idPMR'],
    data () {
        return {
            number: '',
            universite: '',
            adresse: '',
            schoolProof: '',
            PMRProof: '',
            numberRules: [
                v => !!v || 'Veuillez entrer votre numéro de téléphone',
                v => (v && v.length >= 10) || 'Votre numéro de téléphone n\'est pas valide'
            ],
            adresseRules: [
                v => !!v || 'Veuillez entrer votre adresse'
            ],
            universiteRules: [
                v => !!v || 'Veuillez entrer votre SIRET'
            ],
            schoolProofRules: [
                v => !!v || 'Veuillez fournir une attestation de scolarité'
            ],
            PMRProofRules: [
                v => !!v || 'Veuillez fournir une attestation de PMR'
            ]
        }
    },
    computed: {
      email() {
        return this.$store.state.user.email
      }
    },
    methods: {
      handleProfileUpdate() {
        axios
        .put('http://127.0.0.1:8000/api/pmr/'+this.idPmr, { 'id': this.idPmr, 'number': this.number, 'full_adress': this.adresse, 'school_proof': this.schoolProof, 'university': this.universite, 'pmr_proof': this.PMRProof, 'type_user': 'pmr'})
        .then(
          this.$store.state.user.docs_checker = true,
          this.$router.push({ name: 'pmrPage'})
        )
        .catch(error => {
          console.log(error)
        })
      }
    }

}
</script>

<style>

</style>