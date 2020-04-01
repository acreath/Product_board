<template>
  <div class="hello table-responsive ">
    <table class="table">
        <thead>
            <tr class="active">
                <th style="vertical-align: middle;">标题</th>
                <th style="vertical-align: middle;">作者</th>
                <th style="vertical-align: middle;">作者描述</th>
                <th style="vertical-align: middle;">发表时间</th>
                <th style="vertical-align: middle;">阅读数</th>
                <th style="vertical-align: middle;">收藏数</th>
                <th style="vertical-align: middle;">点赞数</th>
                <th style="vertical-align: middle;">评论数</th>
                <th style="vertical-align: middle;">操作</th>
            </tr>
        </thead>
        <tbody v-for="item in content_list" v-bind:key="item.id">
          <tr style="height:50px">
            <td style="width:260px;word-break:break-all;vertical-align: middle;">{{item['title']}}</td>
            <td style="vertical-align: middle;">{{item['author']}}</td>
            <td style="vertical-align: middle;">{{item['author_des']}}</td>
            <td style="vertical-align: middle;">{{item['date']}}</td>
            <td style="vertical-align: middle;" class="success">{{item['views']}}</td>
            <td style="vertical-align: middle;">{{item['loves']}}</td>
            <td style="vertical-align: middle;">{{item['zans']}}</td>
            <td style="vertical-align: middle;">{{item['comment_num']}}</td>
            <td style="vertical-align: middle;"><a v-bind:href="item['url']" target="view_window">详情</a></td>
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
