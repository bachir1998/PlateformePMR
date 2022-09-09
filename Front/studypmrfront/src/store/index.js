import { createStore } from 'vuex'

export default createStore({
  state: {
    user: null,
    logementSelectionne: null,
    logements: [
      { id: '1', residence_name: 'La grande voile', src: require('../assets/lagrandevoile.jpg'), area: '30', adress: '5bis boulevard de Berlin', city: 'Nantes', zip_code: 44000, description: 'residence étudiante dédiée aux personnes à mobilité réduite', prix: 400, bailleurId: 1, flex: 4 },
      { id: '2', residence_name: 'Résidence étudiante Studéa Yléo', src: require('../assets/studea.jpeg'), area: '27', adress: '8 Rue Konrad Adenauer', city: 'Nantes', zip_code: 44000, description: 'Centre d hébergement pour étudiants à mobilité réduite à Nantes', prix: 390, bailleurId: 2, flex: 4 },
      { id: '3', residence_name: 'Résidence étudiante Nantes Ducs de Bretagne', src: require('../assets/ducs.jpg'), area: '30', adress: '4 Rue Emile Pehant', city: 'Nantes', zip_code: 44000, description: 'Centre d hébergement pour étudiants à mobilité réduite à Nantes', prix: 400, bailleurId: 3, flex: 4 },
      { id: '4', residence_name: 'Résidence étudiante Nantes Tourville', src: require('../assets/tourville.jpg'), area: '30', adress: '11 Rue Bias', city: 'Nantes', zip_code: 44000, description: 'residence étudiante dédiée aux personnes à mobilité réduite', prix: 400, bailleurId: 3, flex: 4 },
      { id: '5', residence_name: 'Résidence étudiante Odalys Campus Île de Nantes', src: require('../assets/odalys.jpg'), area: '30', adress: '3 All. Pauline Isabelle Utile', city: 'Nantes', zip_code: 44200, description: 'residence étudiante dédiée aux personnes à mobilité réduite', prix: 420, bailleurId: 4, flex: 4 }
    ],
    listDeLogementsSelectionnes : null,
    pmr: [],
    bailleur: []
  },
  getters: {
  },
  mutations: {
    SET_USER (state, user) {
      if (state.user !== user) {
        state.user = user
      }
    },
    SET_LOGEMENTSELECTIONNE (state, logementSelectionne) {
      state.logementSelectionne = logementSelectionne
    },
    SET_LISTE_DE_LOGEMENTS_SELECTIONNES (state, logements) {
      state.listDeLogementsSelectionnes = logements
      console.log(state.listDeLogementsSelectionnes)
    },
    ADD_PMR (state, pmr) {
      state.pmr.push(pmr)
    },
    ADD_BAILLEUR (state, bailleur) {
      state.bailleur.push(bailleur)
    }
  },
  actions: {
    setUser ({ commit }, user) {
      commit('SET_USER', user)
    },
    /*saveUser ({commit}, email, role) {
      axios.post()
    }*/
    setLogementSelectionne ({ commit }, id) {
      const logement = this.state.logements.find(logement => logement.id == id)
      commit('SET_LOGEMENTSELECTIONNE', logement)
    },
    setLogementsSelectionnes({ commit }, idBailleur) {
      const logements = []
      for(const logement of this.state.logements) {
        if (logement.bailleurID == idBailleur){
          logements.push(logement)
        }
      }
      commit('SET_LISTE_DE_LOGEMENTS_SELECTIONNES', logements)
    },
    addUser({ commit }, user) {
      if(user.role == 'pmr') {
        commit('ADD_PMR', user)
      }
      else {
        commit('ADD_BAILLEUR', user)
      }
    }
  },
  modules: {
  }
})
