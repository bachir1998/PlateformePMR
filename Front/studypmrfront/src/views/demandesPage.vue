<template>
  <v-table height="300px" class="my-6">
    <thead>
      <tr>
        <th class="text-left">
          Email
        </th>
        <th class="text-left">
          Numéro de téléphone
        </th>
        <th class="text-left">
          Logement
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="item in demandes"
        :key="item.email"
      >
        <td>{{ item.email }}</td>
        <td>{{ item.number }}</td>
        <td><router-link :to="{name: 'logementPage', params: { idLogement: item.id }}" style="text-decoration: none; color: black;">Voir logement</router-link></td>
      </tr>
    </tbody>
  </v-table>
</template>

<script>
  export default {
    data () {
      return {
      }
    },
  }
</script>