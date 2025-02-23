<script>
	import '../app.css';
	let { children } = $props();
</script>

<main class="block max-w-2xl md:w-full md:mx-auto mx-2">
	{@render children()}
</main>


<nav class="bg-gray-400 flex justify-around w-screen">
	<a class="p-2" href="/">Home</a>
	<a class="p-2" href="/adkar">adkar</a>
	<a class="p-2" href="/misbaha">misbaha</a>
</nav>
