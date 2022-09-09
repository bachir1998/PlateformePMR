import axios from 'axios'
import { createStore } from 'vuex'

export default createStore({
  state: {
    user: null,
    logementSelectionne: null,
    logements: [],
    listDeLogementsSelectionnes : null
  },
  getters: {
  },
  mutations: {
    SET_USER (state, user) {
      if (state.user !== user) {
        state.user = user
      }
    },
    SET_LOGEMENTS (state, logements) {
      state.logements = logements
    },
    SET_LOGEMENTSELECTIONNE (state, logementSelectionne) {
      state.logementSelectionne = logementSelectionne
    },
    SET_LISTE_DE_LOGEMENTS_SELECTIONNES (state, logements) {
      state.listDeLogementsSelectionnes = logements
      console.log(state.listDeLogementsSelectionnes)
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
    setLogements ({ commit }) {
      axios.get('http://127.0.0.1:8000/api/logement').then(result => {
        commit('SET_LOGEMENTS', result.data)
      })
    }
  },
  modules: {
  }
})
