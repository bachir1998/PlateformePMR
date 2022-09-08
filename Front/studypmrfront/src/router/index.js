import { createRouter, createWebHistory } from 'vue-router'
import Connexion from '../views/connexionPage.vue'
import Inscription from '../views/inscriptionPage.vue'
import Logements from '../views/logementsPage.vue'
import Logement from '../views/logementPage.vue'
import Accueil from '../views/accueilPage.vue'
import Bailleur from '../views/bailleurPage.vue'
import Profile from '../views/profilePage.vue'
import ProfilePMR from '../views/profilePMRPage.vue'
import Demandes from '../views/demandesPage.vue'
import Annonces from '../views/annoncesPage.vue'

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
    props: true,
    component: Logement
  },
  {
    path: '/accueil',
    name: 'accueil',
    component: Accueil
  },
  {
    path: '/bailleur',
    name: 'bailleurPage',
    component: Bailleur,
    props: true
  },
  {
    path: '/profile/:idBailleur',
    name: 'profilePage',
    component: Profile,
    props: true
  },
  {
    path: '/profilePMR/:idPMR',
    name: 'profilePMRPage',
    component: ProfilePMR,
    props: true
  },
  {
    path: '/demandes',
    name: 'demandesPage',
    component: Demandes
  },
  {
    path: '/annonces/:idBailleur',
    name: 'annoncesPage',
    component: Annonces,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
