<template>
<v-card
    class="mx-auto"
  >
    <v-container fluid class="my-6">
      <v-row dense>
        <v-col
          cols=4
        >
    <v-hover
      v-slot="{ isHovering, props }"
    >
    <v-card
        class="mx-auto"
        max-width="350"
        :elevation="isHovering ? 12 : 2"
        v-bind="props"
    >
    <router-link :to="{name: 'profilePage', params: { idBailleur: user.user_id }}" style="text-decoration: none;">
        <v-img
        class="align-end text-white"
        height="200"
        src="../assets/profile.jpg"
        cover
        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
        width="350px"

        >
            <center><v-card-title style="margin-bottom: 25%"><h1>PROFILE</h1></v-card-title></center>
        </v-img>
    </router-link>
    </v-card>
    </v-hover>
        </v-col>
        <v-col
          cols=4
        >
    <v-hover
      v-slot="{ isHovering, props }"
    >
    <v-card
        class="mx-auto"
        max-width="350"
        :elevation="isHovering ? 12 : 2"
        v-bind="props"
    >
    <router-link :to="{name: 'demandesPage', params: { idBailleur: user.user_id }}" style="text-decoration: none;">
        <v-img
        class="align-end text-white"
        height="200"
        src="../assets/demandes.jpg"
        cover
        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
        width="350px"

        >
            <center><v-card-title style="margin-bottom: 25%"><h1>DEMANDES</h1></v-card-title></center>
        </v-img>
      </router-link>
    </v-card>
    </v-hover>
        </v-col>
        <v-col
          cols=4
        >
    <v-hover
      v-slot="{ isHovering, props }"
    >
    <v-card
        class="mx-auto"
        max-width="350"
        :elevation="isHovering ? 12 : 2"
        v-bind="props"
    >
    <router-link :to="{name: 'annoncesPage', params: { idBailleur: user.user_id }}" style="text-decoration: none;">
        <v-img
        class="align-end text-white"
        height="200"
        src="../assets/annonces.jpg"
        cover
        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
        width="350px"

        >
            <center><v-card-title style="margin-bottom: 25%"><h1>MES ANNONCES</h1></v-card-title></center>
        </v-img>
      </router-link>
    </v-card>
    </v-hover>
        </v-col>
      </v-row>
    </v-container>
</v-card>
</template>

<script>
export default {
    data () {
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