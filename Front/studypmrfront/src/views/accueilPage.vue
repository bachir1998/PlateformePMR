<template>
  <v-card
    class="mx-auto"
  >
    <v-container fluid class="my-6">
      <v-row dense>
        <v-col
          v-for="logement in logements"
          :key="logement.title"
          :cols="logement.flex"
        >
          <v-card>

            <v-card-title v-text="logement.title"></v-card-title>
            <v-card-subtitle>
              1,000 miles of wonder
            </v-card-subtitle>

            <v-card-actions>
               
              <v-btn size="small" color="surface-variant" variant="text" icon="mdi-heart"></v-btn>
               
              <v-spacer></v-spacer>

              <v-btn variant="outlined" color="warning" @click="this.$router.push({ name: 'logementPage', params: { idLogement: logement.id } })">
                  Plus de détails
                </v-btn>

              <!--<v-btn size="small" color="surface-variant" variant="text" icon="mdi-bookmark"></v-btn>

              <v-btn size="small" color="surface-variant" variant="text" icon="mdi-share-variant"></v-btn>-->
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
    name: 'accueilPage',
    data: () => ({
    }),
    computed: {
      logements () {
        return this.$store.state.logements
      }
    }


}
</script>

<style>

</style>