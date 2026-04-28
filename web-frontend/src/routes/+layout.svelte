<script lang="ts">
    import favicon from '$lib/assets/favicon.svg';

    import './layout.css';

    let { children } = $props();
</script>

<svelte:head><link rel="icon" href={favicon} /></svelte:head>

<main class="min-h-screen bg-mandalay-900 p-6 font-lora sm:p-12 lg:p-24">
    {@render children()}
</main>
