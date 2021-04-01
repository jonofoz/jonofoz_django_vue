<template>
  <div class="container">
    <router-link to="/posts"><button class="btn btn btn-primary">Back to Posts</button></router-link>
    <router-link :to="{ name: 'edit-post', params: { slug: post.slug }}" action="edit"><button type="submit" class="btn btn-default"> Edit </button></router-link>
    <hr>
    <h1><span class="green-text">{{ post.title }}</span></h1>
    <p align="center">
      <!-- <img src="https://i.imgur.com/SA8cjs8.png" @click="getBlogPosts"> -->
    </p>
    <div>
        {{ post.body }}
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      user: this.$store.state.auth.profile,
      post: {
        title: '...'
      }
    }
  },
  methods: {
    async getBlogPost () {
      const userID = this.user.id
      await fetch(`http://localhost:8000/api/posts?user-id=${userID}`)
        .then(res => res.json())
        .then(res => res.filter(post => post.slug === this.$route.params.slug)[0])
        .then(post => { this.post = post })
    }
  },
  created () {
    this.getBlogPost()
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
