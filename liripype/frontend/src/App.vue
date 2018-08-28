<template>
  <div id="app">
    <header class="container-fluid">
      <!-- <div class="row">
        <div class="col-xl-2">
          <img alt="Vue logo" src="./assets/logo.png" id="main_logo">
        </div> -->
        <div class="container">
        <!-- <nav class="navbar navbar-light bg-light">
          <a class="navbar-brand" href="#">

            Bootstrap
          </a>
        </nav> -->
        <b-navbar toggleable="md" type="dark" variant="info">

          <b-navbar-brand href="#">
            <img src="./assets/logo.png" width="30" height="30" class="d-inline-block align-top" alt="">
          </b-navbar-brand>

          <b-collapse is-nav id="nav_collapse">

            <b-navbar-nav>
              <b-nav-item href="#">Link</b-nav-item>
              <b-nav-item href="#" disabled>Disabled</b-nav-item>
            </b-navbar-nav>

            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto">

              <b-nav-form>
                <b-form-input size="sm" class="mr-sm-2" type="text" placeholder="Search"/>
                <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
              </b-nav-form>
              <router-link to="/">Home</router-link>
              <router-link to="/about">About</router-link>
              <b-nav-item-dropdown right>
                <!-- Using button-content slot -->
                <template slot="button-content">
                  <em>User</em>
                </template>
                <b-dropdown-item href="#">Profile</b-dropdown-item>
                <b-dropdown-item href="#">Signout</b-dropdown-item>
              </b-nav-item-dropdown>
            </b-navbar-nav>

          </b-collapse>
          <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
        </b-navbar>

      </div>

    </header>

    <div class="container">
      <router-view/>
    </div>

    <footer class="container">
    </footer>
  </div>
</template>

# STYLE

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 10px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
#main_logo{
  max-height: 4em;
  margin-right: 5em;
}
/* Remove the navbar's default rounded borders and increase the bottom margin */
.navbar {
  margin-bottom: 50px;
  border-radius: 0;
}

header {
  margin-bottom: 0;
  padding: 1em;
  max-height: 100px;
  background-color: red;
}
/* Add a gray background color and some padding to the footer */
footer {
  background-color: #f2f2f2;
  padding: 25px;
}
router-link {
  margin-right: 100em;
}
</style>
