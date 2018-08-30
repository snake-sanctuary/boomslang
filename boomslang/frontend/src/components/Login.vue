<template>
  <div>
    <h1>{{ msg }}</h1>
    <h2>Login</h2>
      <form @submit.prevent="postPost" method="POST">
        <input type="text" @keyup="checkUsername" name="username" required="required">
        <input type="password" name="password" required="required">
        <input type="submit" class="btn btn-primary" value="Submit">
      </form>
    Not a member?<a href="#">Sign up</a>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      msg: 'Login page'
    }
  },
  methods: {
    checkUsername () {

    },
    postPost () {
      this.axios.post(`api/login`, {
        body: this.value
      })
    .then(response => {})
    .catch(e => { this.errors.push(e) })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
