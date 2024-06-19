<script setup lang="ts">
import { computed } from 'vue'
import { formatDate } from '@/components/article/ArticleHelper'
import { useArticleStore } from '@/stores/article'
import type { Article } from '@/types/article'

const props = defineProps<{
  id: number
}>()
const article: Article = useArticleStore().getArticleById(props.id)

const articleDate = computed(() => formatDate(article.publishedAt))
</script>

<template>
  <v-sheet>
    <v-row>
      <v-col cols="12">
        <v-card>
          <v-img :src="article.urlToImage" height="200">
            <v-row class="fill-height" align="center">
              <v-col>
                <v-card-title class="text-h5 white--text">
                  {{ article.title }}
                </v-card-title>
                <v-card-subtitle class="white--text">
                  {{ articleDate }}
                </v-card-subtitle>
              </v-col>
            </v-row>
          </v-img>
          <v-card-text>
            {{ article.content }}
          </v-card-text>
          <v-card-actions> </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-sheet>
</template>
