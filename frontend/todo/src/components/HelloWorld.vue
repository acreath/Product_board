<template>
  <div class="hello">
    <table class="table table-hover table-responsive table-striped">
        <thead>
            <tr>
                <th >文章标题</th>
                <th >作者</th>
                <th>作者描述</th>
                <th >发表时间</th>
                <th >阅读数</th>
                <th >收藏数</th>
                <th >点赞数</th>
                <th >评论数</th>
                <th >操作</th>
            </tr>
        </thead>
        <tbody v-for="item in content_list" v-bind:key="item.id">
          <tr>
            <td>{{item['title']}}</td>
            <td>{{item['author']}}</td>
            <td>{{item['author_des']}}</td>
            <td>{{item['date']}}</td>
            <td>{{item['views']}}</td>
            <td>{{item['loves']}}</td>
            <td>{{item['zans']}}</td>
            <td>{{item['comment_num']}}</td>
            <td><a v-bind:href="item['url']" target="view_window">详情</a></td>
          </tr>
        </tbody>
    </table>
  <div style="float:right" >
    <ul class="pagination" v-for="n in num_page" v-bind:key="n.id">
      <li style="float:left" v-bind:class="{active: active[n]}" v-on:click="get_content(n)"><a >{{n}}</a></li>
    </ul>
  </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HelloWorld',
  data () {
    return {
      content_list: [],
      num_page:[],
      active:[]
    }
  },
  created () {
    
    const path = 'http://127.0.0.1:5000/1'
    axios.get(path)
      .then((res) => {
        console.log(res.data)
        this.content_list = res.data['list']
        this.num_page = res.data['num_page']
      })
      .catch((error) => {
        console.error(error)
      })
      for (var i=0; i<this.num_page.length;i++)
      {
        this.active[i] = ''
      }
  },
  methods:{
    get_content:function (num) {
      
      const path = 'http://127.0.0.1:5000/' + num
      axios.get(path)
      .then((res) => {
        console.log(res.data)
        this.content_list = res.data['list']
        this.num_page = res.data['num_page']
      })
      .catch((error) => {
        console.error(error)
      })

      for (var i=0; i<this.num_page.length;i++)
      {
        this.active[i] = ''
      }
      this.active[num] = 'active'
    }
  }
}
</script>
