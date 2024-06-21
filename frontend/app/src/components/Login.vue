<template>
  <div class="container">
    <h1>Login</h1>
    <form @submit.prevent="login">
      <label for="username">Username</label>
      <input id="username" v-model="username" placeholder="Username">
      <label for="password">Password</label>
      <input id="password" type="password" v-model="password" placeholder="Password">
      <button type="submit">Login</button>
    </form>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
import api from '../api';

export default {
  data() {
    return {
      username: '',
      password: '',
      error: '',
    };
  },
  methods: {
    async login() {
      try {
        const response = await api.login({ username: this.username, password: this.password });
        localStorage.setItem('token', response.data.access);
        this.$router.push('/clientes');
      } catch (error) {
        this.error = 'Falha no login. Verifique suas credenciais.';
      }
    }
  }
};
</script>

<style scoped>
.error {
  color: red;
}
</style>
