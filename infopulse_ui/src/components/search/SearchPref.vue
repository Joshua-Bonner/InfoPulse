<script setup lang="ts">
import { ref, watchEffect } from 'vue'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const searchPref = ref(userStore.userSearchPref)

watchEffect(() => {
  searchPref.value = userStore.userSearchPref
})
</script>

<template>
  <v-dialog width="auto">
    <v-card title="USER SEARCH PREFERENCES" width="800px" density="compact">
      <v-card-item density="compact">
        <v-card-title>Search in: </v-card-title>
        <v-container>
          <v-row justify="space-between">
            <v-col cols="4">
              <v-switch v-model="searchPref!.search_in" value="title" label="Title"></v-switch>
            </v-col>
            <v-col cols="4">
              <v-switch
                v-model="searchPref!.search_in"
                value="description"
                label="Description"
              ></v-switch>
            </v-col>
            <v-col cols="4">
              <v-switch v-model="searchPref!.search_in" value="content" label="Content"></v-switch>
            </v-col>
          </v-row>
        </v-container>
      </v-card-item>
      <v-card-item density="compact">
        <v-card-title>Search from: </v-card-title>
        <v-text-field v-model="searchPref!.search_from" append-inner-icon="mdi-calendar">
        </v-text-field>
      </v-card-item>
      <v-card-item density="compact">
        <v-card-title>Search to: </v-card-title>
        <v-text-field v-model="searchPref!.search_to" append-inner-icon="mdi-calendar">
        </v-text-field>
      </v-card-item>
      <v-card-item density="compact">
        <v-card-title>Sort by: </v-card-title>
        <v-select v-model="searchPref!.sort_by" :items="['relevancy', 'popularity', 'publishedAt']">
        </v-select>
      </v-card-item>
      <v-card-actions>
        <v-btn @click="() => userStore.updateSearchPref()">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
