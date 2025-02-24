<script>
	let {
		dikr = 'سبحان الله وبحمده',
		dikr_count
	} = $props();

	let count = $state(0);

	function countUp() {
		if (count >= dikr_count) return;
		count += 1;
	}
</script>

<div class="text-center flex flex-col content-between items-center h-max">
	<h3>{dikr}</h3>
	<button
		class="bg-green-300 rounded-full size-20 p-3 text-2xl font-semibold block mt-32"
		onclick={count += 1}
	>
		{count}
	</button>
</div>

