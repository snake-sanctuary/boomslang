<template>
  <div class="container">
    <b-navbar toggleable="md">
      <b-navbar-brand href="#">
        <img src="../assets/logo.png" width="30" height="30" class="d-inline-block align-top" alt="Logo">
      </b-navbar-brand>

      <b-collapse is-nav id="nav_collapse">

        <b-navbar-nav>
          <b-nav-item href="#">Link</b-nav-item>
          <b-nav-item href="#" disabled>Disabled</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <b-nav-item-dropdown right>
            <!-- Using button-content slot -->
            <template slot="button-content">
              <em>User</em>
            </template>
            <b-dropdown-item href="#"><router-link to="/profile">Profile</router-link>Profile</b-dropdown-item>
            <b-dropdown-item href="#" @click="signout">Signout</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>

      </b-collapse>
      <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
    </b-navbar>

  </div>
</template>

<script>
export default {
  name: 'Navbar',
  data () {
    return {
    }
  },
  methods: {
    signout () {
      console.log('Signed Out')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* Remove the navbar's default rounded borders and increase the bottom margin */

</style>
