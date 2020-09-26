import { Component } from '@angular/core';
import { Doc, NawahService, Res } from 'ng-nawah';
import { Observable } from 'rxjs';

@Component({
	selector: 'app-home',
	templateUrl: './home.component.html',
	styleUrls: ['./home.component.css']
})
export class HomeComponent {

	blogs$: Observable<Res<any>> = this.nawah.call({
		endpoint: 'blog/read'
	});

	comments$: {
		[key: string]: Observable<Res<any>>
	} = {}

	comment: {
		name: string;
		email: string;
		content: string;
	} = {
			name: '',
			email: '',
			content: ''
		};

	constructor(private nawah: NawahService) { }

	loadComments(blog_id: string): void {
		this.comments$[blog_id] = this.nawah.call({
			endpoint: 'blog_comment/read',
			query: [{ blog: blog_id }]
		});
	}

	createComment(blog_id: string): void {
		this.nawah.call({
			endpoint: 'blog_comment/create',
			doc: { ...this.comment, blog: blog_id }
		}).subscribe({
			next: (res) => {
				alert(res.msg);
			},
			error: (res: Res<Doc>) => {
				alert(res?.msg);
			}
		});
	}

}
