<template>
  <div class="container">
    <h1><span class="green-text">{{ action }} Post</span></h1>
    <p align="center">
      <!-- <img src="https://i.imgur.com/SA8cjs8.png" @click="getBlogPosts"> -->
    </p>
    <div class="row">

        <div class="col-md-8 col-md-offset-2">

            <form action="" method="POST">

                <div class="form-group has-error">
                    <label for="slug">Slug <span class="require">*</span> <small>(This field use in url path.)</small></label>
                    <input type="text" class="form-control" name="slug" />
                    <span class="help-block">Field not entered!</span>
                </div>

                <div class="form-group">
                    <label for="title">Title <span class="require">*</span></label>
                    <input type="text" class="form-control" name="title" />
                </div>

                <div class="form-group">
                    <label for="description">Description</label>
                    <textarea rows="5" class="form-control" name="description" ></textarea>
                </div>

                <div class="form-group">
                    <p><span class="require">*</span> - required fields</p>
                </div>

                <div class="form-group">
                    <button type="submit" class="btn btn-primary">
                        {{ action }}
                    </button>
                    <button class="btn btn-default">
                        Cancel
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
      post: {},
    }
  },
  methods: {
    async getBlogPosts () {
      const userID = this.$store.state.auth.profile.id
      await fetch(`http://localhost:8000/api/posts?user=${userID}`)
        .then(res => res.json())
        .then(posts => { this.posts = posts })
    }
  },
  created () {
    this.getBlogPosts()
  },
  computed: {
        action: function(){
          const action = this.$props.action;
          if (action == "edit"){
            return "Update";
          }
          else if (action == "add"){
            return "Create"
          }
          else {
            console.log(action);
          }
        }
    },
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
