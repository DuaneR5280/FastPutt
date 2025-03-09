import { createRouter, createWebHistory } from 'vue-router';

// Import views
const Home = () => import('../views/Home.vue');
const Scores = () => import('../views/Scores.vue');
const Courses = () => import('../views/Courses.vue');

// Define routes
const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/scores',
        name: 'Scores',
        component: Scores
    },
    {
        path: '/courses',
        name: 'Courses',
        component: Courses
    }
];

// Create router instance
const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

export default router;
