<template>
  <v-card
    class="mx-auto my-6"
    max-width="700"
    max-height="1000"
  >
   
    <v-card-title v-text="logementSelectionne.residence_name"></v-card-title>

    <v-card-subtitle v-text="logementSelectionne.adress + ', ' + logementSelectionne.zip_code + ', ' + logementSelectionne.city">
    </v-card-subtitle>

    <v-divider></v-divider>

    <v-card-text>
      <img 
            :src= "logementSelectionne.src"
            cover
            />
            <h3 v-text="'Loyer : '+ logementSelectionne.prix"></h3>
            <p v-text="logementSelectionne.description"></p>
    </v-card-text>

    <v-card-actions>
               
      <v-btn size="small" color="surface-variant" variant="text" icon="mdi-heart"></v-btn>
               
      <v-spacer></v-spacer>

      <v-btn variant="outlined" color="success" v-show="user" @click="reserver">
          Réserver
      </v-btn>
      <v-btn variant="outlined" color="success" v-show="!user" disabled>
          Réserver
      </v-btn>
    </v-card-actions>
    <v-divider></v-divider>
      <router-link v-show="!user" :to="{name: 'connexionPage'}" style="text-decoration: none; color: black;"><marquee><h6>Connectez-vous pour réserver!</h6></marquee></router-link>
  </v-card>
</template>

<script>
export default {
    props: ['idLogement'],
    name: 'logementPage',
    data: () => ({
      show: false
    }),
    computed: {
      logementSelectionne () {
        return this.$store.state.logementSelectionne
      },
      user () {
        return this.$store.state.user
      }
    },
    beforeMount() {
      this.$store.dispatch('setLogementSelectionne', this.idLogement)
    },
    methods: {

    }

}
</script>

<style>

</style>