<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <h1 class="text-h3 font-weight-bold mb-4">Disc Golf Courses</h1>
                <p class="text-body-1 mb-6">Browse and discover disc golf courses</p>
            </v-col>

            <!-- Course filtering options -->
            <v-col cols="12">
                <v-card class="mb-6 pa-4">
                    <v-card-title>Find Courses</v-card-title>
                    <v-row>
                        <v-col cols="12" md="4">
                            <v-text-field v-model="searchTerm" label="Search by name" prepend-icon="mdi-magnify"
                                variant="outlined" density="comfortable"></v-text-field>
                        </v-col>
                        <v-col cols="12" md="4">
                            <v-select v-model="selectedDifficulty" :items="difficulties" label="Difficulty"
                                variant="outlined" density="comfortable"></v-select>
                        </v-col>
                        <v-col cols="12" md="4">
                            <v-select v-model="selectedHoles" :items="holeOptions" label="Number of Holes"
                                variant="outlined" density="comfortable"></v-select>
                        </v-col>
                    </v-row>
                </v-card>
            </v-col>

            <!-- Course listings -->
            <v-col v-for="course in courses" :key="course.id" cols="12" md="6" lg="4">
                <v-card class="mb-4">
                    <v-img :src="course.image" height="200" cover></v-img>

                    <v-card-title>{{ course.name }}</v-card-title>

                    <v-card-text>
                        <div class="d-flex mb-2">
                            <v-rating :model-value="course.rating" color="amber" density="compact" size="small"
                                readonly></v-rating>
                            <span class="text-grey ml-2">({{ course.reviewCount }} reviews)</span>
                        </div>

                        <div class="mb-2">
                            <v-icon size="small" color="primary">mdi-map-marker</v-icon>
                            <span class="ml-1">{{ course.location }}</span>
                        </div>

                        <div class="mb-2">
                            <v-icon size="small" color="primary">mdi-golf</v-icon>
                            <span class="ml-1">{{ course.holes }} holes</span>
                        </div>

                        <div>
                            <v-icon size="small" color="primary">mdi-arrow-up-down</v-icon>
                            <span class="ml-1">{{ course.difficulty }}</span>
                        </div>
                    </v-card-text>

                    <v-card-actions>
                        <v-btn variant="text" color="primary">View Details</v-btn>
                        <v-spacer></v-spacer>
                        <v-btn variant="text" color="primary">
                            <v-icon>mdi-heart-outline</v-icon>
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
import { ref } from 'vue';

// Filtering state
const searchTerm = ref('');
const selectedDifficulty = ref(null);
const selectedHoles = ref(null);

// Filter options
const difficulties = ['Beginner', 'Intermediate', 'Advanced', 'Professional'];
const holeOptions = ['9 Holes', '18 Holes', '24+ Holes'];

// Sample course data
const courses = ref([
    {
        id: 1,
        name: 'Riverside Disc Golf Course',
        location: 'Portland, OR',
        holes: 18,
        difficulty: 'Intermediate',
        rating: 4.5,
        reviewCount: 128,
        image: 'https://via.placeholder.com/500x300?text=Riverside+Disc+Golf'
    },
    {
        id: 2,
        name: 'Pine Valley Fields',
        location: 'Seattle, WA',
        holes: 24,
        difficulty: 'Advanced',
        rating: 4.8,
        reviewCount: 96,
        image: 'https://via.placeholder.com/500x300?text=Pine+Valley+Fields'
    },
    {
        id: 3,
        name: 'Lakeside Park',
        location: 'San Francisco, CA',
        holes: 9,
        difficulty: 'Beginner',
        rating: 4.1,
        reviewCount: 54,
        image: 'https://via.placeholder.com/500x300?text=Lakeside+Park'
    }
]);
</script>

<style scoped>
/* Add custom styles here */
</style>
