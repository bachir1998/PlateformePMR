<template>
  <v-card
    class="mx-auto my-6"
    max-width="344"
  >
   
    <v-card-title v-text="logementSelectionne.title"></v-card-title>

    <v-card-subtitle>
      1,000 miles of wonder
    </v-card-subtitle>

    <v-divider></v-divider>

    <v-card-text>
      I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
    </v-card-text>

    <v-card-actions>
               
      <v-btn size="small" color="surface-variant" variant="text" icon="mdi-heart"></v-btn>
               
      <v-spacer></v-spacer>

      <v-btn variant="outlined" color="success" v-show="user">
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
    }

}
</script>

<style>

</style>