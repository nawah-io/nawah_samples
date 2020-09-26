import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Doc, NawahService, Res } from 'ng-nawah';

@Component({
	selector: 'app-admin-blog-edit',
	templateUrl: './admin-blog-edit.component.html',
	styleUrls: ['./admin-blog-edit.component.css']
})
export class AdminBlogEditComponent implements OnInit {

	doc: {
		title: {
			ar_AE: string;
			en_AE: string;
		},
		content: {
			ar_AE: string;
			en_AE: string;
		},
	} = {
			title: {
				ar_AE: undefined,
				en_AE: undefined,
			},
			content: {
				ar_AE: undefined,
				en_AE: undefined,
			},
		};

	msg: {
		type?: 'success' | 'fail';
		content?: string;
	} = {};


	constructor(private nawah: NawahService, private route: ActivatedRoute) { }

	ngOnInit() {
		this.nawah.call({
			endpoint: 'blog/read',
			query: [{ _id: this.route.snapshot.params._id }]
		}).subscribe({
			next: (res: Res<Doc>) => {
				this.doc.title = res.args.docs[0].title;
				this.doc.content = res.args.docs[0].content;
			}
		});
	}

	updateBlogPost(): void {
		this.msg = {};
		this.nawah.call({
			endpoint: 'blog/update',
			query: [{ _id: this.route.snapshot.params._id }],
			doc: this.doc
		}).subscribe({
			next: (res) => {
				this.msg = {
					type: 'success',
					content: res.msg
				};
			},
			error: (res: Res<Doc>) => {
				this.msg = {
					type: 'fail',
					content: res.msg || (res as any)
				};
			}
		});
	}

}
