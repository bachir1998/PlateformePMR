<template>
  <v-app>
    <navbar/>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

import navbar from './components/NavBar.vue'
export default {
  name: 'App',
  data: () => ({
    //
  }),
  components: {
    navbar
  },
}
</script>
