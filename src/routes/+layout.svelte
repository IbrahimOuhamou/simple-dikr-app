<script>
	import '../app.css';
	let { children } = $props();
</script>

<main class="block max-w-2xl md:mx-auto mx-2">
	{@render children()}
</main>
