<script>
	import '../app.css';
	let { children } = $props();
</script>

<main class="block max-w-2xl md:w-full md:mx-auto mx-2 max-h-screen">
	{@render children()}
</main>


<nav class="bg-gray-400 flex justify-around w-screen">
	<a class="p-2" href="/" aria-label="Home">
		<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-house"><path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
	</a>
	<a class="p-2" href="/misbaha">Misbaha</a>
</nav>
