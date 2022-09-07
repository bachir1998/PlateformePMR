import { createRouter, createWebHistory } from 'vue-router'
import Connexion from '../views/connexionPage.vue'
import Inscription from '../views/inscriptionPage.vue'
import Logements from '../views/logementsPage.vue'
import Logement from '../views/logementPage.vue'
import Accueil from '../views/accueilPage.vue'

const routes = [
  {
    path: '/connexion',
    name: 'connexionPage',
    component: Connexion
  },
  {
    path: '/inscription',
    name: 'inscriptionPage',
    component: Inscription
  },
  {
    path: '/logements',
    name: 'logementsPage',
    component: Logements
  },
  {
    path: '/logement/:idLogement',
    name: 'logementPage',
    component: Logement
  },
  {
    path: '/accueil',
    name: 'accueil',
    component: Accueil
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
