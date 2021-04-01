<template>
  <div class="container">

    <router-link to="/posts"><button class="btn btn btn-primary">Back to Posts</button></router-link>
    <hr>
    <h1><span class="green-text">{{ actionText }} Post</span></h1>
    <p align="center">
      <!-- <img src="https://i.imgur.com/SA8cjs8.png" @click="getBlogPosts"> -->
    </p>
    <div class="row">
        <div class="col-md-8 col-md-offset-2">
            <form @submit.prevent="submitForm">
                <div class="form-group has-error">
                    <label for="slug">Slug</label>
                    <input type="text" class="form-control" name="slug" v-model="post.slug" />
                </div>
                <div class="form-group">
                    <label for="title">Title</label>
                    <input type="text" class="form-control" name="title" v-model="post.title" />
                </div>

                <div class="form-group">
                    <label for="description">What's up, {{ user.full_name }}?</label>
                    <textarea rows="5" class="form-control" name="body" v-model="post.body"></textarea>
                </div>

                <div class="form-group">
                    <button type="submit" class="btn btn-primary">
                        {{ actionText }}
                    </button>
                    <button class="btn btn-default">
                        Cancel
                    </button>
                    <button class="btn btn-danger" @click="deletePost">
                        Delete
                    </button>
                </div>

            </form>
        </div>

    </div>
  </div>
</template>

<script>
export default {
  name: 'AddBlogPost',
  props: ['action'],
  data () {
    return {
      user: this.$store.state.auth.profile,
      post: {
        user_id: this.$store.state.auth.profile.id
      },
      posts: {}
    }
  },
  methods: {
    async getBlogPosts () {
      const userID = this.user.id
      await fetch(`http://localhost:8000/api/posts?user-id=${userID}`)
        .then(res => res.json())
        .then(posts => { this.posts = posts })
    },
    async getBlogPost () {
      const userID = this.user.id
      await fetch(`http://localhost:8000/api/posts?user-id=${userID}`)
        .then(res => res.json())
        .then(res => res.filter(post => post.slug === this.$route.params.slug)[0])
        .then(post => { this.post = post })
    },
    submitForm () {
      if (!this.post.id) {
        this.createPost()
      } else {
        this.updatePost()
      }
    },
    async createPost () {
    //  console.log(this.user);
    //  console.log(this.post);
      const { slug, title, body } = this.post
      if (slug.length && title.length && body.length) {
        this.getBlogPosts()
        await fetch('http://localhost:8000/api/posts/', {
          method: 'post',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.post)
        }).then(() => {
          this.$router.push('http:/localhost:8080/posts')
        }).catch(e => console.log(e))
      }
    },
    async updatePost () {
      this.getBlogPosts()
      await fetch(`http://localhost:8000/api/posts/${this.post.id}/`, {
        method: 'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.post)
      }).then(() => {
        this.$router.push('http:/localhost:8080/posts')
      }).catch(e => console.log(e))
    },
    async deletePost () {
      this.getBlogPosts()
      await fetch(`http://localhost:8000/api/posts/${this.post.id}/`, {
        method: 'delete',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.post)
      }).then(() => {
        this.$router.push('http:/localhost:8080/posts')
      })
    }
  },

  created () {
    this.getBlogPosts()
    if (this.$route.params.slug) {
      this.getBlogPost()
    }
  },
  computed: {
    actionText: function () {
      const action = this.$props.action
      if (action === 'edit') {
        return 'Update'
      } else if (action === 'add') {
        return 'Create'
      } else {
        console.log(action)
      }
    }
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
