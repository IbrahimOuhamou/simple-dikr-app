<script>
	let { data } = $props();
	const adkar = data.adkar;
	console.log(JSON.stringify(data.adkar));
</script>

<div>
	{#each adkar as dikr}
		<div>
			<p>{dikr.value}</p>
			<p>{dikr.count}</p>
		</div>
	{/each}
</div>

