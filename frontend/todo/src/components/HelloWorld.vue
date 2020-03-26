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
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HelloWorld',
  data () {
    return {
      content_list: []
    }
  },
  created () {
    const path = 'http://127.0.0.1:5000/'
    axios.get(path)
      .then((res) => {
        console.log(res.data)
        this.content_list = res.data['list']
      })
      .catch((error) => {
        console.error(error)
      })
  }
}
</script>
