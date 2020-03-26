<template>
  <div>
    <button type="button" class="btn btn-primary" v-on:click="getMessage">{{msg}}</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  el: '#test',
  data () {
    return {
      msg: 'This is test'
    }
  },
  methods: {
    getMessage () {
      const path = 'http://0.0.0.0:5000/test'
      axios.get(path)
        .then((res) => {
          this.msg = res.data
        })
        .catch((error) => {
          console.error(error)
        })
    }
  }

}
</script>
