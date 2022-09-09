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
            </v-card-subtitle>

            <v-card-actions>
               
              <v-btn size="small" color="surface-variant" variant="text" icon="mdi-heart"></v-btn>
               
              <v-spacer></v-spacer>

              <v-btn
                variant="outlined"
                size="medium"
                icon
                color="warning accent-3"
                >
                <v-icon>mdi-pencil</v-icon>
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
    props: ['idBailleur'],
    data: () => ({
    }),
    computed: {
      logements () {
        return this.$store.listDeLogementsSelectionnes
      }
    }

}
</script>

<style>

</style>