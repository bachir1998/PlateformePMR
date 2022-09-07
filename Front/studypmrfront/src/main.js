import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import { initializeApp } from 'firebase/app'

loadFonts()

const firebaseConfig = {
  apiKey: "AIzaSyCp7wjJvX0Vb_L0XU7nnZiWXl8iT48oZu0",
  authDomain: "studypmr-7b44e.firebaseapp.com",
  projectId: "studypmr-7b44e",
  storageBucket: "studypmr-7b44e.appspot.com",
  messagingSenderId: "815579180600",
  appId: "1:815579180600:web:3f2bfd5e50acf8bcb640cd"
};

initializeApp(firebaseConfig)

createApp(App)
  .use(router)
  .use(store)
  .use(vuetify)
  .mount('#app')
