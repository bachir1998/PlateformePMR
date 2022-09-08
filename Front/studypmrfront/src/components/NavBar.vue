<template>
  <v-app-bar app color="warning accent-3">
      <v-toolbar-title>
        <router-link to="/accueil" style="text-decoration: none; color: white;">
          <span class="font-weight-dark">Study</span>
          <span style="color: #008fba" class="font-weight-light">PMR</span>
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn variant="outlined" color="white" class="mx-1" v-show="user" @click="signoutButtonPressed">Se déconnecter</v-btn>
      <v-btn variant="outlined" color="white" class="mx-1" v-show="!user" @click="this.$router.push({ name: 'connexionPage'})">Se connecter</v-btn>
      <v-btn variant="outlined" color="white" class="mx-1" v-show="!user" @click="this.$router.push({ name: 'inscriptionPage'})">S'inscrire</v-btn>
      <v-btn variant="outlined" color="white">A propos</v-btn>
    </v-app-bar>
</template>

<script>
import { getAuth } from 'firebase/auth'
export default {
  computed: {
    user () {
      return this.$store.state.user
    }
  },
  methods: {
    signoutButtonPressed (e) {
      e.stopPropagation()
      getAuth().signOut().then(() => {
        this.$store.dispatch('setUser', null)
      })
      this.$router.push({ name: 'accueil' })
    }
  }

}
</script>

<style>

</style>