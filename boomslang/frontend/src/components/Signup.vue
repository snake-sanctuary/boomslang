<template>
  <div>
    <h1>{{ msg }}</h1>
    <h2>Login</h2>
      <form @submit.prevent="postPost" method="POST">
        <ul>
          <li><input type="email" name="username" @keyup="checkEmail" required="required"></li>
          <li><input type="text" name="first_name" required="required"></li>
          <li><input type="text" name="last_name" required="required"></li>
          <li><input type="password" name="password" required="required"></li>
          <li><input type="submit" class="btn btn-primary" value="Sign up"></li>
        </ul>
      </form>
  </div>
</template>

<script>
export default {
  name: 'Signup',
  data () {
    return {
      msg: 'Signup page'
    }
  },
  methods: {
    postPost () {
      this.axios.post(`api/signup`, {
        body: this.postBody
      }).then(response => {
        console.log(response.content)
      }).catch(e => { this.errors.push(e) })
    },

    checkUsername () {
      console.log(this.value)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
