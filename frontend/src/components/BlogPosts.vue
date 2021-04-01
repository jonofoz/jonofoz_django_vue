<template>
  <div class="container">
    <h1><span class="green-text">{{ user.full_name }}'s</span> Blog</h1>
    <p align="center">
      <!-- <img src="https://i.imgur.com/SA8cjs8.png" @click="getBlogPosts"> -->
    </p>
    <ul id="blog-list">
      <li v-for="post in posts" :key="post.id">
        <hr>
        <br>
        <h3>
          <router-link :to="{ name: 'read-post', params: { slug: post.slug}}">{{ post.title }}</router-link> |
          <router-link :to="{ name: 'edit-post', params: { slug: post.slug }}" action="edit"><font-awesome-icon icon="pen-square" /></router-link>
        </h3>
        <p class="last-updated">Updated {{ post.updated_at }}</p>
        <div>
          {{ shorten(post.body) }}
        </div>
      </li>
      <hr>
    </ul>

  </div>
</template>

<script>
export default {
  name: 'BlogPosts',
  data () {
    return {
      user: this.$store.state.auth.profile,
      posts: {}
    }
  },
  methods: {
    async getBlogPosts () {
      const userID = this.$store.state.auth.profile.id
      console.log(userID)
      await fetch(`http://localhost:8000/api/posts?user-id=${userID}`)
        .then(res => res.json())
        .then(posts => { this.posts = posts })
    },
    shorten (text) {
      if (text.length > 300) {
        return `${text.slice(0, 300)} ...`
      } else {
        return text
      }
    }
  },
  created () {
    this.getBlogPosts()
  }
}
</script>

<style>
  #blog-list {
    list-style-type: none;
  }
  .green-text{
    background: -webkit-linear-gradient(45deg, #41B883, #35485D);
    background-color: #41B883;
    background-size: 100%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    -moz-background-clip: text;
    -moz-text-fill-color: transparent;
  }
  .last-updated {
   font-style: italic;
   color: grey;
 }
</style>
