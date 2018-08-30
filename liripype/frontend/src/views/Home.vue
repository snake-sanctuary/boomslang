<template>
  <div class="home">
    <SearchBox/>
    <HelloWorld msg="Welcome to Your Vue.js App"/>

  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import SearchBox from '@/components/SearchBox.vue'

export default {
  name: 'home',
  components: {
    HelloWorld,
    SearchBox
  }
}
</script>
