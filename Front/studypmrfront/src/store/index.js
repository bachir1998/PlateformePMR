import { createStore } from 'vuex'

export default createStore({
  state: {
    user: null,
    logementSelectionne: null,
    logements: [
      { id : 1, title: 'Logement Capge ',  flex: 4 },
      { id : 2, title: 'Logement Epsi ', flex: 4 },
      { id : 3, title: 'Logement Ynov', flex: 4 },
      { id : 4, title: 'Logement Capge', flex: 4 },
      { id : 5, title: 'Logement Efrei',  flex: 4 },
      { id : 6, title: 'Logement Franck',flex: 4 },
    ],
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
    }
  },
  modules: {
  }
})
