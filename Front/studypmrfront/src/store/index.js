import { createStore } from 'vuex'

export default createStore({
  state: {
    user: null
  },
  getters: {
  },
  mutations: {
    SET_USER (state, user) {
      if (state.user !== user) {
        state.user = user
      }
    }
  },
  actions: {
    setUser ({ commit }, user) {
      commit('SET_USER', user)
    },
    /*saveUser ({commit}, email, role) {
      axios.post()
    }*/
  },
  modules: {
  }
})
