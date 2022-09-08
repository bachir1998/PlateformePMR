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

      <v-btn variant="outlined" color="success">
          Réserver
      </v-btn>

    </v-card-actions>
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
        console.log('computed', this.$store.state.logementSelectionne)
        return this.$store.state.logementSelectionne
      }
    },
    beforeMount() {
      this.$store.dispatch('setLogementSelectionne', this.idLogement)
    }

}
</script>

<style>

</style>