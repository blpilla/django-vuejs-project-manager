<template>
  <div id="app">
    <nav>
      <router-link to="/login">Login</router-link>
      <router-link to="/clientes" v-if="isAuthenticated">Clientes</router-link>
      <router-link to="/projetos" v-if="isAuthenticated">Projetos</router-link>
      <router-link to="/atividades" v-if="isAuthenticated">Atividades</router-link>
      <button v-if="isAuthenticated" @click="logout">Sair</button>
    </nav>
    <router-view/>
    <footer>
      Gerenciador de Projetos 2024
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      isAuthenticated: !!localStorage.getItem('token'),
    };
  },
  watch: {
    '$route'() {
      this.isAuthenticated = !!localStorage.getItem('token');
    }
  },
  created() {
    if (!this.isAuthenticated && this.$route.path !== '/login') {
      this.$router.push('/login');
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('token');
      this.isAuthenticated = false;
      this.$router.push('/login');
    }
  }
};
</script>

<style src="./assets/styles.css"></style>
