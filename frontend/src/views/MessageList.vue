<template>
  <v-container>
    <v-row>
      <v-col cols="3">
        <v-sheet rounded="lg">
          <v-list rounded="lg">
            <v-list-item 
              v-for="(item, index) in groups.values" 
              :key="index" 
              @click="findMessage(item)"
              :title="`${item['title']}`"
            >
            </v-list-item>

            <v-divider class="my-2"></v-divider>

            <v-list-item color="grey-lighten-4" link title="Refresh"></v-list-item>
          </v-list>
        </v-sheet>
      </v-col>

      <v-col>
        <v-sheet min-height="70vh" rounded="lg" class="pa-3">
          <v-row v-if="messages.values.length === 0">
            <v-col>投稿がありません</v-col>
          </v-row>
          <v-card
            v-else
            class="ma-4"
            v-for="(item, index) in messages.values" 
            :key="index"
          >
            <v-card-title class="ma-3">
              <v-row>
                <v-avatar class="mt-2 ml-2" color="grey-darken-1" size="36"></v-avatar>
                <v-col class="text-subtitle-1">{{ getUser(item['owner']) }}</v-col>
                <v-spacer></v-spacer>
                <v-spacer></v-spacer>
                <v-spacer></v-spacer>
                <v-col class="text-caption">{{ format(item['pub_date']) }}</v-col>
              </v-row>
            
            </v-card-title>
            <v-card-text class="mx-2 text-body-1">{{ item['content'] }}</v-card-text>

            <v-card-actions class="mx-3">
              <v-row>
                <v-col>
                  <v-btn icon="mdi-thumb-up"></v-btn>{{ item['good_count'] }}
                </v-col>
                <v-col>
                  <v-btn icon="mdi-share-variant"></v-btn>{{ item['share_count'] }}
                </v-col>
              </v-row>
            </v-card-actions>
          </v-card>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import axios from 'axios';
import dayjs from 'dayjs';
import { onMounted, reactive } from 'vue';

interface Group {
  owner: number,
  title: string
}

interface Message {
  owner: number,
  group: number,
  content: string,
  share_id: number,
  share_count: number,
  good_count: number,
  pub_date: Date,
}

interface User {
  id: number,
  username: string,
  first_name: string,
  last_name: string,
  email: string
}

const groups: Array<Group> = reactive([])
const myGroups: Array<User> = reactive([])
const messages: Array<Message> = reactive([])
const users: Array<User> = reactive([])

const findMessage = (group: Group) => {
  const param = {
    owner: group.owner,
    title: group.title
  }
  axios.get('http://127.0.0.1:8000/api/message/', { params: param })
    .then((response) => {
      messages.values = response.data
    }).catch((error) => {
      console.log(error)
    }) 
}

const findGroup = () => {
  axios.get('http://127.0.0.1:8000/api/groups/')
    .then((response) => {
      groups.values = response.data
    }).catch((error) => {
      console.log(error)
    })
}

const findMyGroup = () => {
  axios.get('http://127.0.0.1:8000/api/mygroup/')
    .then((response) => {
      myGroups.values = response.data
      console.log(myGroups)
    }).catch((error) => {
      console.log(error)
    })
}

const findUser = ()=> {
  axios.get('http://127.0.0.1:8000/api/users/')
    .then((response) => {
      const newUsers: Array<User> = response.data
      newUsers.filter((user: User) => !users.map(v => v.id).includes(user.id)).forEach((user: User) => {
        users.push(user)
      });
    }).catch((error) => {
      console.log(error)
    })
}

const getUser = (id: number) => {
  return users.find(v => v.id === id)?.username
}

const format = (date: Date) => {
  return dayjs(date).format("YYYY/MM/DD HH:MM")
}

onMounted(() => {
  findUser(),
    findGroup(),
  findMyGroup()
})

</script>
