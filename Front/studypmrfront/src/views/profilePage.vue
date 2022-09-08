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
          <v-form @submit.prevent="handleEmailSignup" ref="form">
            <v-card-text>
              <v-text-field
                v-model="name"
                :rules="nameRules"
                type="text"
                label="Nom complet ou nom d'usage si entreprise"
                placeholder="Nom complet ou nom d'usage (si entreprise)"
                prepend-inner-icon="mdi-account"
                disabled
              />
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
                type="number"
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
                v-model="siret"
                :rules="siretRules"
                type="text"
                label="SIRET"
                placeholder="33070384400036"
                prepend-inner-icon="mdi-numeric"
                required
              />
            </v-card-text>
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
export default {
    props: ['idBailleur'],
    data () {
        return {
            name: "younesselghazi",
            email:"younesselghazi@gmail.com",
            number: '',
            siret: '',
            adresse: '',
            numberRules: [
                v => !!v || 'Veuillez entrer votre numéro de téléphone',
                v => (v && v.length >= 10) || 'Votre numéro de téléphone n\'est pas valide'
            ],
            adresseRules: [
                v => !!v || 'Veuillez entrer votre adresse'
            ],
            siretRules: [
                v => !!v || 'Veuillez entrer votre SIRET'
            ]
        }
    }

}
</script>

<style>

</style>