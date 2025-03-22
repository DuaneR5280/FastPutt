import { createRouter, createWebHistory } from 'vue-router';

// Import views
const Home = () => import('../views/Home.vue');
const Scores = () => import('../views/Scores.vue');
const Games = () => import('../views/Games.vue');
const GameSummary = () => import('../components/GameSummary.vue');
const JYLY = () => import('../components/JYLY.vue');
const TenTwentyFive = () => import('../components/TenTwentyFive.vue');
const c1 = () => import('../components/c1.vue');
const c1results = () => import('../components/c1results.vue');

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
        path: '/games',
        name: 'Games',
        component: Games
    },
    {
        path: '/games/:id',
        name: 'GameSummary',
        component: GameSummary
    },
    {
        path: '/jyly',
        name: 'JYLY',
        component: JYLY
    },
    {
        path: '/1025',
        name: 'TenTwentyFive',
        component: TenTwentyFive
    },
    {
        path: '/c1',
        name: 'c1',
        component: c1
    },
    {
        path: '/c1results/:gameId',
        name: 'c1results',
        component: c1results
    },
    {
        path: '/c2',
        name: 'c2',
        component: c1
    }
];

// Create router instance
const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

export default router;
