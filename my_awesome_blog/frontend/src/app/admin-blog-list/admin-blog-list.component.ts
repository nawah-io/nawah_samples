import { Component, OnInit } from '@angular/core';
import { Doc, NawahService, Res } from 'ng-nawah';

@Component({
	selector: 'app-admin-blog-list',
	templateUrl: './admin-blog-list.component.html',
	styleUrls: ['./admin-blog-list.component.css']
})
export class AdminBlogListComponent implements OnInit {

	blogs: Array<Doc> = [];

	constructor(private nawah: NawahService) { }

	ngOnInit() {
		this.readPosts();
	}

	readPosts(): void {
		this.nawah.call({ endpoint: 'blog/read' }).subscribe({
			next: (res) => {
				this.blogs = res.args.docs;
			},
			error: (err: Res<Doc>) => {
				alert(`Unexpected error occurred: ${err.msg || err}`);
			}
		});
	}

	deletePost(_id: string): void {
		if (confirm('Are you sure you want to delete this blog post?')) {
			this.nawah.call({
				endpoint: 'blog/delete',
				query: [{
					_id: _id
				}]
			}).subscribe({
				next: (res) => {
					this.readPosts();
				},
				error: (err: Res<Doc>) => {
					alert(`Unexpected error occurred: ${err.msg || err}`);
				}
			});
		}
	}

}
