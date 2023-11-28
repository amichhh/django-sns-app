<template>
  <v-app id="app">
    <v-app-bar flat>
      <v-container class="mx-auto d-flex align-center justify-center">
        <v-avatar class="me-4 " color="grey-darken-1" size="32"></v-avatar>

        <v-btn variant="text" @click="router.push('/')">Dashboard</v-btn>
        <v-btn variant="text" @click="router.push('/messages')">Messages</v-btn>
        <v-btn variant="text">Profile</v-btn>
        <v-btn variant="text">Updates</v-btn>

        <v-spacer></v-spacer>

        <v-responsive max-width="160">
          <v-text-field density="compact" flat hide-details label="Search" rounded="lg" single-line
            variant="solo-filled"></v-text-field>
        </v-responsive>
      </v-container>
    </v-app-bar>

    <v-main class="bg-grey-lighten-3">
      <RouterView />
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter()

</script>