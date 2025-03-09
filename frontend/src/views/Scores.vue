<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <h1 class="text-h3 font-weight-bold mb-4">Scores</h1>
                <p class="text-body-1 mb-6">Track and analyze your disc golf performance</p>

                <!-- Placeholder for scores table -->
                <v-card>
                    <v-card-title>
                        Your Recent Scores
                        <v-spacer></v-spacer>
                        <v-text-field v-model="search" append-icon="mdi-magnify" label="Search" single-line
                            hide-details></v-text-field>
                    </v-card-title>
                    <v-data-table :headers="headers" :items="scores" :search="search" class="elevation-1">
                    </v-data-table>
                </v-card>
            </v-col>

            <v-col cols="12" class="mt-6">
                <v-btn color="primary" size="large">
                    <v-icon left>mdi-plus</v-icon>
                    Add New Score
                </v-btn>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
import { ref } from 'vue';

// Sample data for the scores table
const search = ref('');
const headers = ref([
    { title: 'Date', key: 'date' },
    { title: 'Course', key: 'course' },
    { title: 'Score', key: 'score' },
    { title: 'Par', key: 'par' },
    { title: 'Actions', key: 'actions', sortable: false }
]);
const scores = ref([
    { date: '2025-03-01', course: 'Riverside Park', score: 54, par: 58 },
    { date: '2025-02-25', course: 'Highland Woods', score: 63, par: 62 },
    { date: '2025-02-18', course: 'Pine Valley', score: 72, par: 68 },
    { date: '2025-03-02', course: 'Pine Valley', score: 67, par: 68 }
]);
</script>

<style scoped>
/* Add custom styles here */
</style>
