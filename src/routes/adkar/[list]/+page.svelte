<script>
	import Dikr from '$lib/Dikr.svelte'

	let { data } = $props();
	// const adkar = data.adkar;

	let adkar = $state(data.adkar);
	function removeFn(index) {
		adkar = [...adkar.slice(0, index), ...adkar.slice(index + 1)];
	}
</script>

<div>
	{#each adkar as dikr, i (adkar[i])}
		<Dikr {...dikr} i={i} {removeFn}/>
	{/each}
</div>
