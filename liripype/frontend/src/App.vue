<template>
  <div id="app">
    <header class="container-fluid">
        <Navbar/>
    </header>

    <div class="container">
      <router-view/>
    </div>

    <footer class="container-fluid" id="footer">
      <div class="footer_top">
      </div>
      <div class="footer_bottom">
      </div>
    </footer>
  </div>
</template>

# SCRIPT

<script>

import Navbar from '@/components/Navbar.vue'
export default {
  name: 'app',
  components: {
    Navbar
  }
}
</script>

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

  header {
    margin-bottom: 0;
    padding: 1em;
    max-height: 100px;
    background-color: #0073b7;
  }
  /* Add a gray background color and some padding to the footer */
  #footer {
    padding-right: 0px;
    padding-left: 0px;
    min-height: 10em;
  }

  .footer_top {
    background-color: #0073b7;
    min-height: 5em;
  }
  .footer_bottom {
    background-color: #006dad;
    min-height: 5em;
  }
</style>
