import dikr_data from '$lib/data.json';

export function load({ params }) {
    return {
        dikr_data: dikr_data,
    };
}


export const ssr = false;
// export const prerender = true;
