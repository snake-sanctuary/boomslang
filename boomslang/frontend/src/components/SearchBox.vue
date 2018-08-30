<template>
  <div id="search-box" class="container-fluid">
    <h2>JUMBOTRON</h2>
    <div class="container">
      <div class="search-bar">
        <b-form-input class="col-md-8" v-model="pkg_name" type="text" placeholder="Enter the package name">
        </b-form-input>
        <font-awesome-icon icon="coffee" />
      </div>
      <div class="input-group input-group-newsletter">
                      <input class="form-control" placeholder="Enter email..." aria-label="Enter email..." aria-describedby="basic-addon" type="email">
                      <div class="input-group-append">
                        <button class="btn btn-secondary" type="button">Notify Me!</button>
                      </div>
                    </div>
  </div>
  </div>
</template>

<script>
export default {
  name: 'SearchBox',
  data () {
    return {
      pkg_name: ''
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#search-box {
  margin-top: 30px;
  margin-bottom: 30px;
}

.search-bar {
  position: relative;
}

</style>
